---
name: stb-bwa-sus-bilanz-pruefung
description: "Workflow-Skill zu stb bwa sus bilanz pruefung. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# BWA-, SuSa- und Bilanzprüfung mit Insolvenzreife-Check (§§ 17, 19 InsO, § 102 StaRUG)

## Kernsachverhalt

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kaltstart-Rückfragen

1. Welche Rechtsform und Größenklasse (§ 267 HGB) — UG, GmbH, AG, GmbH & Co. KG?
2. Welche Unterlagen liegen vor — BWA (Standard, Bewegungs-, kumuliert), SuSa, Bilanzentwurf, Anlagenspiegel?
3. Welcher Auswertungsstichtag — Monats-BWA, Quartal, Jahresabschluss?
4. Liegen Liquiditätsdaten vor — kurzfristig fällige Verbindlichkeiten (≤ 3 Wochen), verfügbare Zahlungsmittel, Kreditlinien?
5. Sind Rangrücktritte oder Patronatserklärungen vorhanden? Liegen die Klauseltexte vor?
6. Existieren Steuer- oder SV-Rückstände — Finanzamt, Krankenkassen, Berufsgenossenschaft?
7. Wurde bereits eine Fortbestehensprognose oder ein Sanierungskonzept IDW S 6 erstellt?
8. Ist der Steuerberater mit der Erstellung des Jahresabschlusses beauftragt (§ 102 StaRUG-Auslöser)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Primärnormen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 19 InsO** — Überschuldung: Vermögen deckt Verbindlichkeiten nicht, es sei denn positive Fortbestehensprognose. Prognosezeitraum 24 Monate (SanInsKG, gültig bis 31.12.2026).

**§ 15a InsO** — Insolvenzantragspflicht: 3 Wochen (Zahlungsunfähigkeit), 6 Wochen (Überschuldung).

**§ 15b InsO** — Zahlungsverbote nach Insolvenzreife.

**§ 102 StaRUG** — Hinweis- und Warnpflicht des Steuerberaters bei Erstellung des Jahresabschlusses, wenn offenkundige Anhaltspunkte für Insolvenzgründe vorliegen.

**§ 1 StaRUG** — Krisenfrüherkennung durch Geschäftsleitung haftungsbeschränkter Gesellschaften.

**§§ 252, 264 Abs. 2 HGB** — Going-concern; Grundsatz bei Fortführungsannahme; muss hinterfragt werden wenn Krise erkennbar.

**§ 39 Abs. 2 InsO** — Qualifizierter Rangrücktritt: Verbindlichkeiten im Überschuldungsstatus nicht passiviert.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema BWA/SuSa/Bilanz


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Datenaufnahme und Konsistenzcheck | BWA-Schlusssalden = SuSa-Salden = Bilanzposten; Periodenabgrenzung RAP, Rückstellungen | Konsistenz bestätigt oder Abweichung benannt |
| 2 | SuSa-Auffälligkeiten | Ungewöhnliche Sollsalden Erlöskonten; Habensalden Aufwandskonten; hohe Verrechnungskonten 1590/1599 | Anomalien für Belegstichprobe vormerken |
| 3 | Belegstichprobe | Top-10-Eingangs-/Ausgangsrechnungen; Cut-off-Test kurz vor Stichtag; Kasse (§ 146 AO) | Buchungsgenauigkeit geprüft |
| 4 | Bilanzielle Überschuldungsindizien | Eigenkapital negativ? HGB-Bilanzwerte ≠ Überschuldungsstatus; Liquidationswerte erforderlich | Rechnerische Unterdeckung? |
| 5 | Stille Lasten | Drohende Verluste, Bürgschaften, Garantien, anhängige Prozesse | Rückstellungsbedarf quantifizieren |
| 6 | Stille Reserven | Selbstgeschaffene immaterielle WG; Sachanlagen-Marktwert vs. Buchwert; Forderungsabtretung | Aktivierungsoptionen prüfen |
| 7 | Rangrücktritte | Qualifizierter Rangrücktritt § 39 Abs. 2 InsO → passivseitig herausnehmen; einfacher bleibt | Klauseltext prüfen |
| 8 | Fortbestehensprognose § 19 Abs. 2 InsO | Integrierte Planung 24 Monate (SanInsKG); tragfähiges Konzept; IDW S 6-Elemente | Positiv/Negativ |
| 9 | Zahlungsunfähigkeitsprüfung § 17 InsO | Liquiditätsstatus: fällige Verbindlichkeiten vs. Aktiva I; Quote ≥ 10 %? | Ampel Rot/Gelb/Grün |
| 10 | Steuer- und SV-Rückstände | Finanzamt, Krankenkassen, BG; Stundung § 222 AO vs. AdV § 361 AO | Passiva I korrekt eingestellt |
| 11 | Going concern § 252 HGB | Fortführungsannahme haltbar? Abweichende Annahme bei negativer Prognose | Abweichende Angabe im Abschluss |
| 12 | § 102 StaRUG — Hinweispflicht ausgelöst? | Erstellungsauftrag Jahresabschluss + offenkundige Anhaltspunkte? | Warnschreiben erforderlich |
| 13 | Indizienkatalog § 17 Abs. 2 InsO | SV-Rückstände, Stundungsanträge, Mahnungen, Rücklastschriften, eingestellte Lieferantenzahlungen | Zahlungseinstellung ohne Rechnung möglich |
| 14 | Abschluss und Dokumentation | Befund-Tabelle; Krisenmatrix; ggf. § 102 StaRUG-Hinweisschreiben; Empfehlungen | Ergebnis mit Zeitstempel und Unterschrift |
| 15 | Querverweise andere Skills | Schwere Krise → anwaltliche Prüfung; Liquiditätsvorschau; Warnschreiben | Übergabe und Anschluss |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Krisensignale erkennbar waren | Steuerberater (muss dokumentieren, dass er gewarnt hat) | Warnschreiben, Aktenvermerk, Eingangsbestätigung |
| Qualifizierter Rangrücktritt | Gesellschafter | Klauseltext; § 39 Abs. 2 InsO-Kriterien |
| Fortbestehensprognose positiv | GF / Sachverständiger | Integrierter Finanzplan IDW S 6/S 11 |
| Stille Reserven und Lasten | GF / Gutachter | Bewertungsgutachten; Wertermittlung |
| § 102 StaRUG-Schwelle offenkundig | Steuerberater (Abwehrseite) / Haftungskläger | BWA-Befunde, SuSa-Daten, Zeitpunkt der Erkennbarkeit |

## Typische Gegenargumente

| Gegenargument | Gegenstrategie |
|---|---|
| "Negatives Eigenkapital ist nur buchhalterisch — Stille Reserven gleichen aus" | Stille Reserven konkret quantifizieren; Nachweis durch Sachverständige erforderlich; bloße Behauptung genügt nicht |
| "Going concern rechtfertigt Fortführungsannahme" | § 252 Abs. 1 Nr. 2 HGB: nur solange keine entgegenstehenden Anhaltspunkte; bei Krisensignalen schriftliche Begründung Pflicht |
| "Gesellschafterdarlehen ist nachrangig" | Qualifizierter Rangrücktritt nach § 39 Abs. 2 InsO prüfen; einfacher Rangrücktritt lässt Verbindlichkeit im Status |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — BWA SuSa und Bilanz pruefend | Pruefung nach Schema; Schriftsatz unten |
| Variante A — Nur BWA vorhanden keine Bilanz | BWA-Teilpruefung; Bilanzanforderung nachfragen |
| Variante B — Krisensignale erkennbar Warnschreiben noetig | Warnschreiben-Skill parallel einsetzen |
| Variante C — Pruefung nur zur Jahresabschlusspruefung | Teilpruefung; Jahresabschluss-Fokus setzen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Befund-Tabelle BWA/SuSa

```
BEFUND-TABELLE BWA/SuSa — Stichtag [Datum]
Mandant: [Firma] GmbH

| Konto / Bereich | Auffälligkeit | Mögliche Ursache | Empfehlung |
|---|---|---|---|
| 1590 Verrechnungskonto GF | Saldo EUR [x] | Privatentnahmen ohne Verbuchung | Klärung und Buchung |
| SV-Abgaben-Konto | Kein Buchungsbeleg 3 Monate | SV-Beiträge nicht abgeführt | Sofort zahlen; § 266a StGB |
| Erlöskonten Soll-Saldo | Gutschriften offen | Rückgaben/Stornos nicht verbucht | Beleg anfordern |
| RAP passiv fehlt | Vorauszahlung Miete nicht abgegrenzt | Periodenabgrenzung fehlt | Buchung nachholen |
```

### Baustein 2: Krisenmatrix

```
KRISENMATRIX — [Firma] GmbH — Stichtag [Datum]

| Indikator | Ist-Wert | Schwellenwert | Bewertung | Rechtsfolge |
|---|---|---|---|---|
| Eigenkapital | EUR −[x] | > 0 | KRITISCH | Überschuldungsrisiko |
| Liquidität 1. Grades | [X] % | > 100 % | KRITISCH | § 17 InsO-Risiko |
| SV-Rückstände | EUR [x] | 0 | KRITISCH | § 266a StGB; Passiva I |
| Steuerrückstände | EUR [y] | 0 | ERHÖHT | § 69 AO GF-Haftung |
| Stundungsanträge | [n] in 3 Mon. | 0 | KRITISCH | Indiz Zahlungseinstellung |
| Lieferantenzahlungstage | [x] Tage | ≤ 45 Tage | ERHÖHT | Zahlungsstockung |
| § 17 InsO (Zahlungsunfähigkeit) | Quote [X] % | < 10 % | ROT | Antragsfrist 3 Wochen |
| § 19 InsO (Überschuldung) | EK negativ, keine Prognose | — | ROT | Antragsfrist 6 Wochen |
| § 102 StaRUG (Hinweispflicht) | offenkundig | ausgelöst | JA | Warnschreiben sofort |
```

### Baustein 3: Hinweisschreiben § 102 StaRUG

```
[StB-Briefkopf]                                  [Datum]

PERSÖNLICH / VERTRAULICH

[GmbH, vertreten durch GF Name]

Betreff: Hinweis auf erkennbare Krisensituation — § 102 StaRUG

Sehr geehrte/r Herr / Frau [GF-Name],

aus der von uns geführten laufenden Finanzbuchhaltung und der
betriebswirtschaftlichen Auswertung zum Stichtag [Datum] ergeben sich
folgende Krisensignale, auf die wir Sie hiermit ausdrücklich hinweisen:

1. Eigenkapital negativ — EUR [x] zum Stichtag [Datum].
2. Sozialversicherungsbeiträge für [Monat/Monate] nicht abgeführt:
   EUR [y] (Indiz für Zahlungseinstellung; § 266a StGB-Risiko).
3. Liquiditätslücke von EUR [z] (Quote [X] %) im 3-Wochen-Horizont.

Diese Befunde begründen den begründeten Verdacht einer Krise im Sinne
von § 102 StaRUG und möglicher Insolvenzgründe nach §§ 17, 19 InsO.

Als Geschäftsführer sind Sie verpflichtet, eine rechtliche Prüfung
der Antragspflicht nach § 15a InsO einzuholen. Wir empfehlen
dringend die unverzügliche Konsultation eines Fachanwalts für
Insolvenz-/Sanierungsrecht oder Steuerrecht.

Als Ihr Steuerberater leisten wir mit diesem Schreiben den nach
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Eine rechtliche Beurteilung der Antragspflicht ist uns nach § 5 RDG
nicht erlaubt.

Bitte bestätigen Sie den Eingang dieses Schreibens binnen sieben Tagen.

Mit freundlichen Grüßen
[StB]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Kosten Krisenprüfung | Steuerberater-Gebühren nach StBVV; ggf. Zeithonorar | Auftrag klar vereinbaren |
| Kosten Sachverständigengutachten stille Reserven | EUR 1.500–8.000 je nach Umfang | Lohnt bei größeren Gesellschaften |
| Kosten Sanierungskonzept IDW S 6 | EUR 10.000–50.000+ je nach Komplexität | WP/StB-Kanzlei mit Sanierungserfahrung |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Alle Krisenampeln grün | Dokumentieren; Wiedervorlage 3 Monate; § 102 StaRUG-Pflicht erfüllt |
| Gelbe Ampeln ohne sofortige Insolvenzreife | Warnschreiben § 102 StaRUG; Liquiditätsvorschau beauftragen; Sanierungsoptionen besprechen |
| Rote Ampeln — § 17 oder § 19 InsO indiziert | Warnschreiben sofort; Übergabe an Anwalt für Insolvenzreife-Prüfung; keine Abschlusserstellung ohne Warnung |
| Mandant reagiert nicht auf Warnung | Wiederholung schriftlich; ggf. Mandatsniederlegung § 627 BGB |
| Rangrücktritt möglich | Qualifizierten Rangrücktritt empfehlen; anwaltliche Klauselfassung notwendig |

## Anschluss-Skills

- `anw-insolvenzreife-pruefung-17-19-inso` — anwaltliche Insolvenzreife-Prüfung
- `stb-warnschreiben-krisensignale` — vertieftes Warnschreiben-Skill
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditätsvorschau für § 17 InsO-Prüfung

## Quellen

- InsO §§ 17, 18, 19, 15a, 15b, 39
- HGB §§ 252, 264, 267, 268
- StaRUG §§ 1, 102
- StBerG §§ 1, 33
- RDG § 5
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6 (Sanierungskonzept) / IDW S 11 (Insolvenzeröffnungsgründe)
- K. Schmidt/Herchen, InsO § 17 Rn. 5–35
- Pape/Schaltke, StaRUG § 102 Rn. 8–35

<!-- AUDIT 27.05.2026 | welle 5c | IX ZR 104/18 (familienrechtlich, NJW 2019, 2770 erfunden) ersetzt durch IX ZR 56/22 (BGH 29.06.2023, NJW 2023, 2775 = ZIP 2023, 1740, Drittschutz Hinweis- und Warnpflicht bei moeglichem Insolvenzgrund) -->
