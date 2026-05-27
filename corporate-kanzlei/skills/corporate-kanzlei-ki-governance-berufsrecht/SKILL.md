---
name: corporate-kanzlei-ki-governance-berufsrecht
description: "KI-Governance und Berufsrecht: Rechtliche Rahmenbedingungen fuer den Einsatz von KI-Werkzeugen in Kanzleien. EU-KI-VO (AI Act), BRAO-Verschwiegenheit, Mandanteninformation, Haftung, Qualitaetssicherung. Dokumentation fuer BJR-Schutz."
---

# KI-Governance und Berufsrecht

## Triage — klaere vor KI-Einsatz

1. Welche KI-Werkzeuge werden eingesetzt (generative KI, Dokumentenanalyse, Recherche)?
2. Welche Mandatsdaten werden verarbeitet (anonym, pseudonymisiert, im Klartext)?
3. Werden Daten an externe Server uebertragen? (Datenschutz; Mandatsgeheimnis)
4. Muss der Mandant ueber KI-Einsatz informiert werden?
5. Wer traegt Verantwortung fuer KI-generierte Ergebnisse (Qualitatskontrolle)?
6. EU-KI-VO (AI Act): In welche Risikoklasse faellt der Anwendungsfall?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

- **§ 43a BRAO** — Verschwiegenheitspflicht; mandatsrelevante Daten duerfen nicht an Dritte weitergegeben werden
- **§ 2 BORA** — Berufsrechtliche Sorgfalt; KI-Ergebnisse muessen qualitaetsgesichert werden
- **Art. 6, 9 DSGVO** — Rechtsgrundlage fuer Datenverarbeitung; besondere Kategorien; Auftragsverarbeitung (Art. 28)
- **EU-KI-VO (AI Act, Verordnung (EU) 2024/1689)** — Hochrisiko-KI-Systeme (Art. 6); verbotene KI (Art. 5); Transparenzpflichten
- **§ 93 AktG / § 43 GmbHG** — BJR: Entscheidungen auf KI-Basis muessen angemessen begruendet und kontrolliert sein

## Aktuelle Rechtsprechung

- BGH, Urt. v. 21.01.2022 - V ZR 192/20, NJW 2022, 1009 — Anwaltshaftung fuer falsche Auskuenfte: Anwalt haftet wenn er ungepruefte Ergebnisse (auch von Datenbanken) weitergibt; fuer KI-generierte Ergebnisse gilt gleiches Qualitaetssicherungs-Gebot
- BVerfG, Beschl. v. 08.06.2021 - 1 BvR 2771/18 — Berufsfreiheit Anwalt und technische Hilfsmittel: Einsatz von Werkzeugen ist grundsaetzlich erlaubt; Verantwortlichkeit bleibt beim Anwalt
- CCBE/BRAK Stellungnahme 2023 — Berufsrechtliche Hinweise zu KI in Kanzleien: Mandanteninformation empfohlen; keine Verarbeitung mandatsrelevanter Daten ohne Einwilligung in Drittland-KI-Dienste

## Kommentarliteratur

- Henssler/Pruestell BRAO § 43a Rn. 1 ff. — Verschwiegenheitspflicht und technische Hilfsmittel
- Kühling/Buchner DSGVO Art. 28 — Auftragsverarbeitung bei KI-Diensten
- Wischmeyer, Regulierung kuenstlicher Intelligenz (2020) — EU-KI-VO Ueberblick

## KI-Risikoklassen (EU-KI-VO): Relevanz fuer Kanzleien

| Risikoklasse | Beispiele | Anforderungen |
|---|---|---|
| Unakzeptables Risiko (verboten) | Social Scoring; biometrische Identifizierung Echtzeit | Kein Einsatz |
| Hochrisiko (Art. 6) | Rechtspflege-Entscheidungen; Zugang zu Dienstleistungen | Konformitaetsbewertung; Registrierung; Protokollierung |
| Begrenzte Transparenz | Generative KI (Chatbots); Deepfake | Kennzeichnungspflicht; Transparenz |
| Minimales Risiko | Recherche-Werkzeuge; Textbearbeitung; Zusammenfassung | Freiwillig; keine zwingenden Pflichten |

Kanzlei-Anwendungen (Dokumentenanalyse, Rechercheassistenz): meist minimales bis begrenztes Risiko, wenn kein Endentscheid delegiert wird.

## DSGVO-Compliance fuer KI-Werkzeuge

| Pruefpunkt | Anforderung | Massnahme |
|---|---|---|
| Rechtsgrundlage | Art. 6 I DSGVO | Berechtigtes Interesse oder Einwilligung |
| Auftragsverarbeitung | Art. 28 DSGVO | AVV mit KI-Anbieter abschliessen |
| Datenuebertragung Drittland | Art. 44 ff. DSGVO | Standardvertragsklauseln (SCC); ggf. Anonymisierung |
| Auskunft Betroffener | Art. 15 DSGVO | Mandant kann Auskunft verlangen |
| Privacy by Design | Art. 25 DSGVO | Keine unnoetigen Daten; Pseudonymisierung |

## Schritt-fuer-Schritt-Workflow

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


1. **KI-Werkzeug evaluieren** — Anbieter; Rechenzentrum; Daten-Policies; EU-KI-VO-Einordnung
2. **AVV abschliessen** — mit Anbieter nach Art. 28 DSGVO; Drittland-SCC falls noetig
3. **Mandanteninformation** — bei Verarbeitung personenbezogener oder mandatsrelevanter Daten informieren
4. **Pseudonymisierungs-Protokoll** — Mandantennamen ersetzen; Sachverhalte entpersonalisieren bevor Eingabe in KI
5. **Qualitaetssicherung** — jedes KI-Ergebnis durch Anwalt inhaltlich pruefen; kein blindes Uebernehmen
6. **Dokumentation** — wann wurde KI eingesetzt; wie wurde Ergebnis geprueft; Akte dokumentiert
7. **Fehlerprotokoll** — bei KI-Irrtum: korrigieren; Mandant informieren; Verbesserung

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-Tool-Einsatz in Kanzlei dokumentieren | Einsatz-Dokumentation nach Template unten |
| Variante A — nur Research-Einsatz ohne Mandantendaten | Vereinfachte Dokumentation; DSGVO-Risiko gering |
| Variante B — Mandantendaten werden verarbeitet | Volle Risikoanalyse; AVV und Mandantenhinweis noetig |
| Variante C — KI generiert Schriftsaetze | Pruefpflicht des Anwalts hervorheben; Haftungsklausel erwaegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template KI-Einsatzdokumentation

```
KI-EINSATZDOKUMENTATION
Mandat: [MATTER-NR.]
Aufgabe: [Beschreibung z.B. "Dokumentenanalyse 45 Vertraege im Datenraum"]
KI-Werkzeug: [WERKZEUGNAME, Anbieter, Version]
Datum: [DATUM]

VERWENDETE DATEN:
[ ] Mandatsrelevante Daten verarbeitet — Pseudonymisierung erfolgt am [DATUM]
[ ] Nur allgemeine Rechts-/Sachinformationen

AVV MIT ANBIETER: [Ja, vom DATUM / Nein, bitte nachtragen]

QUALITAETSSICHERUNG:
KI-Output reviewed von: [NAME, Funktion]
Methode: [Stichprobenpruefung X % / Vollpruefung]
Abweichungen von KI-Output: [Keine / Beschreibung der Korrekturen]

MANDANTENINFORMATION:
[ ] Mandant informiert ueber KI-Einsatz am [DATUM]
[ ] Nicht informiert — Begruendung: [Nur allg. Recherche; keine mandantenspez. Daten]

FAZIT: KI-Ergebnisse wurden angemessen geprueft; Eigenverantwortung des Anwalts gewahrt.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Rote Schwellen

- Mandatsrelevante Daten ohne AVV in Drittland-KI-Dienst → DSGVO-Verstoss; Bussgelder
- KI-Ergebnis ohne Qualitaetspruefung weitergegeben → Anwaltshaftung; § 2 BORA
- KI-gestutzte Entscheidung ohne Dokumentation → kein BJR-Schutz (§ 93 AktG)
- EU-KI-VO Hochrisiko-System ohne Konformitaetsbewertung → ab 2026 Bussgeld bis 30 Mio. EUR oder 6 % Weltumsatz

## Quellen

- § 43a BRAO; Art. 6, 9, 28 DSGVO; EU-KI-VO (EU) 2024/1689; § 93 AktG
- BGH V ZR 192/20 (Anwaltshaftung KI-Analogie); BVerfG 1 BvR 2771/18 (Berufsfreiheit)
- Kühling/Buchner DSGVO Art. 28; Wischmeyer, Regulierung KI (2020)
