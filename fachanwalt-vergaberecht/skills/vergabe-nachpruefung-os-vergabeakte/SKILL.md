---
name: vergabe-nachpruefung-os-vergabeakte
description: "Vergabe Nachpruefung OS Vergabeakte im Plugin Fachanwalt Vergaberecht: prüft konkret Aussichten eines Vergabenachprüfungsverfahrens bewerten, Vergabe-OS für Anfaenger und Profis, Vergabeakte und Dokumentationsvermerk für Auftraggeber, Vergabekammer-Termin simulieren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Vergabe Nachpruefung OS Vergabeakte

## Arbeitsbereich

**Vergabe Nachpruefung OS Vergabeakte** ordnet den Fall über die tragenden Prüfungslinien: Aussichten eines Vergabenachprüfungsverfahrens bewerten, Vergabe-OS für Anfaenger und Profis, Vergabeakte und Dokumentationsvermerk für Auftraggeber. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `vergabe-nachpruefung-aussicht` | Aussichten eines Vergabenachprüfungsverfahrens bewerten: Anwalt oder Bieter will vor Antrag Erfolgsaussichten einschaetzen. Normen: §§ 155 ff. GWB (Rechtsschutz), § 160 Abs. 2 GWB (Antragsbefugnis), § 160 Abs. 3 GWB (Ruegerobliegenheit), § 169 GWB (Zuschlagsstopp). Prüfraster: Antragsbefugnis, Praeklusion, Vergabeverstoesse (Eignung, Wertung, Ausschlussgründe), sofortige Beschwerde OLG. Output Erfolgsaussichts-Gutachten, Strategie-Empfehlung. Abgrenzung: Mandats-Triage siehe mandat-triage-vergaberecht; Nachprüfungsantrag selbst siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk. |
| `vergabe-os-master-orchestrator` | Vergabe-OS für Anfaenger und Profis: erkennt Rolle, Schwellenwert, Verfahrensstand, Fristen, Rechtsweg, Dokumentenlage und fuehrt in Padlet, Tabellen, Schriftsatz, Memo oder Vergabeakte. |
| `vergabeakte-dokumentationsvermerk-builder` | Vergabeakte und Dokumentationsvermerk für Auftraggeber aufbauen: Beschaffungsbedarf, Markterkundung, Verfahrenswahl, Eignung, Wertung, Kommunikation, Entscheidungen und Nachvollziehbarkeit. |
| `vergabekammer-termin-simulation` | Vergabekammer-Termin simulieren: Fragenkatalog, Schwachstellen, Vergleichsfenster, Antragstaktik, Mandantenbriefing und Nachterminplan. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `vergabe-nachpruefung-aussicht`

**Fokus:** Aussichten eines Vergabenachprüfungsverfahrens bewerten: Anwalt oder Bieter will vor Antrag Erfolgsaussichten einschaetzen. Normen: §§ 155 ff. GWB (Rechtsschutz), § 160 Abs. 2 GWB (Antragsbefugnis), § 160 Abs. 3 GWB (Ruegerobliegenheit), § 169 GWB (Zuschlagsstopp). Prüfraster: Antragsbefugnis, Praeklusion, Vergabeverstoesse (Eignung, Wertung, Ausschlussgründe), sofortige Beschwerde OLG. Output Erfolgsaussichts-Gutachten, Strategie-Empfehlung. Abgrenzung: Mandats-Triage siehe mandat-triage-vergaberecht; Nachprüfungsantrag selbst siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk.

# Vergabe-Nachprüfung — Erfolgs-Aussichten

## Zweck

Bei einer drohenden oder erfolgten Vergabe-Entscheidung systematisch prüfen, ob der Nachprüfungsantrag bei der Vergabekammer Aussicht hat. Der Skill führt durch alle Zulässigkeits- und Begründetheitsvoraussetzungen und endet mit einer dokumentierten Handlungsempfehlung.

## Kaltstart-Rückfragen

1. Liegt die Vergabe oberhalb des EU-Schwellenwerts (Liefer-/DL-Bund EUR 143000; Kommunen/sonst EUR 221000; Bau EUR 5538000; Sektoren DL EUR 443000)? Bei Unterschreitung: kein GWB-Nachprüfungsweg.
2. Wurde die Vorabinformation nach § 134 GWB empfangen, und wann? Die 10-Kalendertage-Stillhaltefrist läuft ab Versand an alle unterlegenen Bieter — nicht ab Empfang.
3. Wann genau wurde der Vergabeverstoß erkannt? Lag der Fehler schon in Bekanntmachung oder Vergabeunterlagen (dann: Rüge bis Angebotsabgabe), oder erst nach Submission erkennbar (dann: 10 Kalendertage-Frist § 160 Abs. 3 Nr. 1 GWB)?
4. Wurde die Rüge ordnungsgemäß und rechtzeitig erhoben? In welcher Form (Schreiben, E-Mail mit Empfangsbestätigung)?
5. Hat der Auftraggeber die Rüge ausdrücklich abgelehnt oder nicht reagiert? Ab wann lief die 15-Kalendertage-Frist für den Nachprüfungsantrag § 160 Abs. 3 Nr. 4 GWB?
6. Was ist der genaue materielle Vorwurf — Eignungsfehler, Wertungsfehler, ungewöhnlich niedriges Angebot § 60 VgV, rechtswidrige Aufhebung, unzulässige Direktvergabe?
7. Hat der Mandant reale Auftragschance — war sein Angebot nach Ablauf aller Prüfungsschritte das wirtschaftlichste? Drohender Schaden § 160 Abs. 2 GWB?
8. Ist Akteneinsicht § 165 GWB bereits beantragt oder notwendig, um den Vorwurf substanziieren zu können?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 97 GWB** — Grundsatz: Auftraggeber beschaffen Waren und Dienstleistungen im Wettbewerb und im Wege transparenter Vergabeverfahren.
- **§ 106 GWB** — Schwellenwerte: Verordnungsermächtigung; aktuelle Werte durch VO (EU) 2023/1441.
- **§ 122 GWB** — Eignung: Auftraggeber können von Unternehmen als Mindestanforderungen Befähigung und Erlaubnis, wirtschaftliche und finanzielle sowie technische und berufliche Leistungsfähigkeit fordern.
- **§ 123 GWB** — Zwingende Ausschlussgründe: Verurteilung wegen Straftaten wie Bildung krimineller Vereinigungen, Bestechung, Geldwäsche, Steuerhinterziehung (sechsstellig).
- **§ 124 GWB** — Fakultative Ausschlussgründe: schwere berufliche Verfehlung, Wettbewerbsverzerrung, Interessenkonflikt, Schlechtleistung Vorvertrag.
- **§ 127 GWB** — Zuschlag auf das wirtschaftlichste Angebot; Preis-Leistungs-Verhältnis; Zuschlagskriterien bekannt zu machen.
- **§ 134 GWB** — Informations- und Wartepflicht: 10 Kalendertage Stillhaltefrist ab Absendung der Information an unterlegene Bieter; Vertragsschluss vor Ablauf nichtig.
- **§ 160 Abs. 2 GWB** — Antragsbefugnis: Unternehmen kann VK anrufen, wenn Interesse am Auftrag und Verletzung vergaberechtlicher Vorschriften geltend gemacht wird und dadurch Schaden entstanden ist oder zu entstehen droht.
- **§ 160 Abs. 3 GWB** — Rügeobliegenheit/Präklusion: Erkannte Fehler unverzüglich rügen; Fehler aus Bekanntmachung bis Angebotsabgabe; nach Rügen-Ablehnung binnen 15 Kalendertage Nachprüfungsantrag.
- **§ 165 GWB** — Akteneinsicht im Nachprüfungsverfahren; Ausnahme Betriebs- und Geschäftsgeheimnisse.
- **§ 167 GWB** — Entscheidungsfrist: VK entscheidet innerhalb von 5 Wochen; Verlängerung bei Einvernehmen der Beteiligten oder besonderer Schwierigkeit möglich.
- **§ 169 GWB** — Zuschlagsverbot: Auftraggeber darf nach Eingang des Nachprüfungsantrags den Zuschlag nicht erteilen. Bei besonderem öffentlichem Interesse kann VK auf Antrag des AG den Zuschlag gestatten.
- **§ 171 GWB** — Sofortige Beschwerde: Frist 2 Wochen ab Zustellung VK-Beschluss; beim zuständigen OLG-Vergabesenat.
- **§ 181 GWB** — Schadensersatz: Bei schuldhafter Verletzung vergaberechtlicher Vorschriften; Ersatz des Vertrauensschadens (negative Interesse); Erfüllungsinteresse nur ausnahmsweise.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema in Tabellenform

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Rechtsgrundlage | Ergebnis / Konsequenz |
|---|---|---|---|
| 1 | EU-Schwellenwert überschritten? | § 106 GWB; VO (EU) 2023/1441 | Nein → kein GWB-Weg; Ggf. haushaltsrechtlicher Primärrechtsschutz |
| 2 | Öffentlicher Auftraggeber i.S.d. § 99 GWB? | § 99 GWB | Sektorenauftraggeber → SektVO; sonstige → VOB/A oder VgV |
| 3 | Antragsbefugnis § 160 Abs. 2 GWB | Interesse am Auftrag + drohender Schaden | Kein eigenes Angebot abgegeben → i.d.R. keine Befugnis |
| 4 | Rüge ordnungsgemäß und fristgerecht? | § 160 Abs. 3 GWB | Fehlt → Antrag unzulässig; Dokumentation prüfen |
| 5 | 15-Tage-Frist nach Rügen-Ablehnung gewahrt? | § 160 Abs. 3 Nr. 4 GWB | Versäumnis → Antrag unzulässig; keine Wiedereinsetzung |
| 6 | 10-Tage-Stillhaltefrist § 134 GWB läuft noch? | § 134 GWB | Zuschlag bereits erteilt → nur noch § 135 GWB-Nichtigkeitsantrag |
| 7 | Materieller Vergabeverstoß substanziierbar? | §§ 97, 122 ff., 127 GWB; VgV | Konkrete Fehler benennen; Spekulationen reichen nicht |
| 8 | Ungewöhnlich niedriges Angebot Konkurrent? | § 60 VgV | Aufklärungspflicht AG; Ausschluss bei Nichtplausibilität |
| 9 | Eignungsmangel Konkurrent? | §§ 122-125 GWB; § 42 ff. VgV | Eigene Eignung unstreitig? Konkurrent tatsächlich ungeeignet? |
| 10 | Wertungsfehler substanziierbar? | § 127 GWB; §§ 53, 58 VgV | Bewertungsmatrix anfordern; Akteneinsicht § 165 GWB |
| 11 | Aufhebungsgründe rechtmäßig? | § 63 VgV | Keine sachlichen Gründe → rechtswidrige Aufhebung → Schadensersatz |
| 12 | De-facto-Vergabe (Zuschlag ohne Bekanntmachung)? | § 135 Abs. 2 GWB | 30 Tage ab Kenntnis oder 6 Monate ab Vertragsschluss |
| 13 | Erfolgsaussicht Hauptantrag (Untersagung Zuschlag)? | § 169 GWB | Abwägung: öffentliches Interesse vs. Bieter-Schaden |
| 14 | Kostenrisiko VK-Verfahren? | § 182 GWB | Unterliegender trägt Verfahrensgebühren 2500–50000 EUR + gegnerische Anwaltskosten |
| 15 | OLG-Beschwerde vorbereiten? | § 171 GWB | Frist 2 Wochen; aufschiebende Wirkung prüfen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Bieter prueft Erfolgsaussichten eines Nachpruefungsantrags | Erfolgsaussichten-Memo nach Primaer-Sekundaer-Schema; Template unten |
| Variante A — Vergabeverstoß klar aber Auftrag strategisch wichtig | Ruege und Verhandlung mit Vergabestelle vor Antragstellung |
| Variante B — Beweislage duenn nur Indizien für Fehler | Akteneinsicht § 163 GWB beantragen bevor Antrag gestellt wird |
| Variante C — Mandant will schnellen Schadensersatz nicht Auftrag | Schadensersatzklage § 179 GWB als Alternative zum Nachpruefungsantrag |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Rügeschreiben

```
An [Vergabestelle] [Datum]
Betr.: Vergabeverfahren [Bezeichnung], Az. [...]
 Ruege gemaess § 160 Abs. 3 GWB

Sehr geehrte Damen und Herren,

in der Angelegenheit [Vergabe-Kurztitel] zeigen wir an, dass wir die
rechtlichen Interessen der [Bieter-Firma] vertreten.

Hiermit ruegeon wir folgende Vergabeverstoeße unverzueglich nach
Kenntnisnahme:

1. Verstoß gegen § 127 GWB / § 58 VgV (Wertung)
 Das Angebot unserer Mandantin erzielte in Kriterium [X] lediglich
 [Y] Punkte. Die Begruendung ist unzureichend, weil [konkreter
 Vorwurf]. Ein Vergleich der Leistungsbeschreibung mit dem Angebot
 belegt [Seite, Abschnitt]. Richtige Wertung ergaebe [Z] Punkte
 und damit Platz 1.

2. [ggf. weiterer Verstoss]

Wir fordern Sie auf, den Vergabeverstoß abzustellen und das
Vergabeverfahren in den Stand vor der fehlerhaften Wertung
zurueckzuversetzen, hilfsweise das Verfahren aufzuheben und neu
durchzufuehren.

Wir bitten um Stellungnahme bis [Datum — 5 Werktage].

Mit freundlichen Gruessen
[Kanzlei]
```

### Baustein 2 — Anträge im Nachprüfungsantrag

```
I. Antraege

Die Vergabekammer moge beschliessen:

1. Dem Antragsgegner wird untersagt, in dem Vergabeverfahren [Titel]
 den Zuschlag auf das Angebot der Beigeladenen zu erteilen.

2. Dem Antragsgegner wird aufgegeben, das Vergabeverfahren in den
 Stand vor der Wertungsentscheidung vom [Datum] zurueckzuversetzen
 und das Verfahren unter Beachtung der Rechtsauffassung der
 Vergabekammer fortzufuehren.

3. Dem Antragsgegner wird aufgegeben, dem Antragsteller vollstaendige
 Akteneinsicht gemaess § 165 GWB zu gewaehren.

4. Der Antragsgegner traegt die Kosten des Verfahrens einschliesslich
 der notwendigen Aufwendungen des Antragstellers.

5. Die Hinzuziehung eines Rechtsanwalts durch den Antragsteller wird
 für notwendig erklaert.
```

### Baustein 3 — Argumentation ungewöhnlich niedriges Angebot

```
III. Verstoß gegen § 60 VgV — ungewoehnlich niedriges Angebot der
 Beigeladenen

Das Angebot der Beigeladenen liegt um [X] % unter dem naechstguestigen
Angebot (Antragsteller: EUR [A]; Beigeladene: EUR [B]). Diese Spanne
begruendet die Aufklaerungspflicht des Antragsgegners gemaess § 60
Abs. 1 VgV.

Der Antragsgegner hat ausweislich der Vergabedokumentation [keine
Aufklaerung durchgefuehrt / die Aufklaerung war unzureichend: Anlage
K [X]].

Nachweis einer plausibler Kalkulation setzt voraus, dass der Bieter
saemtliche Einzelpreise, Stundenloehne und sonstige Kostenkomponenten
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Der Antragsgegner haette das Angebot gemaess § 60 Abs. 3 VgV
ausschliessen muessen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Antragsbefugnis (Interesse + Schaden) | Antragsteller |
| Rechtzeitigkeit und Inhalt der Rüge | Antragsteller (Schreiben mit Datum) |
| Vergabeverstoß (materiell) | Antragsteller muss schlüssig darlegen |
| Vergabekonformität (Gegenbeweis) | Auftraggeber trägt Vergabeakte vor |
| Geheimhaltungsinteressen Dritter | Beigeladener |
| Ausschlussgrund Konkurrent | Auftraggeber; Selbstreinigung Bieter |

## Fristen und Verjährung

| Frist | Dauer | Anker | Bemerkung |
|---|---|---|---|
| Rüge bei erkennbarem Verstoß in Bekanntmachung | bis Angebotsabgabe | Ablauf Angebotsfrist | § 160 Abs. 3 Nr. 2 GWB |
| Rüge bei sonstigem erkanntem Verstoß | 10 Kalendertage | Kenntnis des Verstoßes | § 160 Abs. 3 Nr. 1 GWB; "unverzüglich" |
| Nachprüfungsantrag nach Rügen-Ablehnung | 15 Kalendertage | Eingang Rügenablehnungsschreiben | § 160 Abs. 3 Nr. 4 GWB |
| Stillhaltefrist § 134 GWB | 10 Kalendertage | Absendung durch AG | Bei e-Vergabe 15 Tage bei Fax/Brief |
| Sofortige Beschwerde OLG | 2 Wochen | Zustellung VK-Beschluss | § 171 GWB |
| Schadensersatz § 181 GWB | 3 Jahre | Kenntnis Vergabeverstoß + Schaden | §§ 195, 199 BGB |
| Nichtigkeitsantrag De-facto-Vergabe | 30 Tage / 6 Monate | Kenntnis / Vertragsschluss | § 135 Abs. 2 GWB |

## Typische Gegenargumente und Reaktion

| Einwand Auftraggeber | Reaktion |
|---|---|
| Rüge nicht rechtzeitig / keine Rüge | Kenntnisnachweis durch Vorlage Informationsschreiben; ggf. § 134 GWB Datum prüfen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Vergabeverstoß bloß rechnerisch nicht relevant | Kausalität genügt; drohender Schaden ausreichend |
| Aufhebung des Verfahrens zulässig | § 63 VgV Aufhebungsgründe abarbeiten; tatsächliche Gründe müssen vorliegen |
| Sofortiger Zuschlag im öffentlichen Interesse | § 169 Abs. 3 GWB Ausnahme; strenge Voraussetzungen; VK entscheidet nach Abwägung |
| Angebot Antragsteller selbst fehlerhaft | Eigene Wertung kontrollieren; ggf. Hilfsbegründung in Antrag aufnehmen |
| Beigeladener hat Selbstreinigung geltend gemacht | § 125 GWB Maßnahmen prüfen; Verhältnismäßigkeit |

## Streitwert und Kosten

- **VK-Gebühren:** § 182 GWB; Gebührensatz 2500 EUR bis 50000 EUR; Bemessung nach Auftragswert und Aufwand.
- **Unterlegener trägt** Verfahrensgebühren und notwendige Aufwendungen der obsiegenden Partei (§ 182 Abs. 3 GWB).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **OLG-Verfahren:** § 171 Abs. 3 GWB; Kosten nach GKG/ZPO; Streitwert = Auftragswert.
- **Schadensersatz § 181 GWB:** Negativinteresse (Angebotskosten, Bearbeitungsaufwand) ohne besonderen Nachweis; Positivinteresse (entgangener Gewinn) nur bei hochgradiger Auftragschance und schuldhafter Verletzung.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Frist noch offen, starker Materialverstoß | Sofort rügen, VK-Antrag vorbereiten, § 169 GWB sichern |
| Rügefrist abgelaufen, Zuschlag noch nicht erteilt | Prüfen ob andere Verstöße nicht präkludiert; notfalls nur Schadensersatz |
| Zuschlag bereits erteilt, Vertrag geschlossen | § 135 GWB bei De-facto-Vergabe oder § 181 GWB Schadensersatz |
| Erfolgsaussicht gering (eigenes Angebot teuer) | Risiko-Aufklärung; VK-Gebühren können Angebot übersteigen |
| Auftraggeber will aufheben | § 63 VgV Aufhebungsgründe prüfen; ggf. negative Feststellungsklage LG |

## Anschluss-Skills

- `fachanwalt-vergaberecht-nachpruefungsantrag-vk` — vollständige Antragsstruktur
- `fachanwalt-vergaberecht-eignungspruefung` — Eignungsfehler als Antragsgrundlage
- `fachanwalt-vergaberecht-it-sicherheits-vergabe-bsi-it-sig-2` — IT-Vergabe-Spezifika

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vertiefung: Output-Template Erfolgsaussichten-Memo

### Triage — Bevor losgelegt wird, klaere:

1. Ist Ruege nach § 160 Abs. 3 GWB rechtzeitig erhoben worden?
2. Hat Bieter Antragsbefugnis (am Verfahren beteiligt oder haette beteiligt sein koennen)?
3. Welcher Fehler ist konkret nachweisbar (Wertung / Eignung / Diskriminierung / Transparenz)?
4. Liegt der Verstoss kausal für die Nichtberucksichtigung des Mandanten?
5. Werden Chancen geschaetzt: "Keine konkreten Aussichten" → Schadensersatz § 181 GWB statt NPA?

### Output-Template Erfolgsaussichten-Memo
**Adressat:** Mandant — Tonfall: klar erklärend, realistisch

```
ERFOLGSAUSSICHTEN-MEMO Vergaberecht
=========================================
Mandant: [NAME]
Verfahren: [BEZEICHNUNG]
Datum Memo: [TT.MM.JJJJ]

1. Sachverhalt-Kurzfassung:
 [...]

2. Nachgewiesener Vergabeverstoß:
 [§ XY GWB / VgV: Konkrete Verletzung]

3. Chancen Nachpruefungsantrag:
 HOCH / MITTEL / GERING / KEINE
 Begruendung: [Leitsatz-Referenz / Beweislage]

4. Alternativ Schadensersatz § 181 GWB:
 Voraussetzungen erfuellt: JA / NEIN
 Schadenshoehe (geschaetzt): EUR [BETRAG]

5. Empfehlung:
 [NPA einreichen / Schadensersatzklage / Kein weiteres Vorgehen]

6. Fristen:
 Nachpruefungsantrag bis: [TT.MM.JJJJ]
 Beschwerde bis (OLG): [TT.MM.JJJJ bei VK-Entscheidung]
=========================================
```

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `vergabe-os-master-orchestrator`

**Fokus:** Vergabe-OS für Anfaenger und Profis: erkennt Rolle, Schwellenwert, Verfahrensstand, Fristen, Rechtsweg, Dokumentenlage und fuehrt in Padlet, Tabellen, Schriftsatz, Memo oder Vergabeakte.

# Vergabe-OS Master-Orchestrator

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll die gesamte Beschaffung oder den gesamten Rechtsschutzfall vom ersten Satz bis zum naechsten verwertbaren Output steuern. Er arbeitet für Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zuständigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Kurzbild, Phasenkarte, Fristenampel, Skill-Routing, Arbeitsplan, Mandantennaechstschritt.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` für Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `nachpruefungsantrag-powerdraft` für VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` für komplexe Mehrthemenfaelle.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `vergabeakte-dokumentationsvermerk-builder`

**Fokus:** Vergabeakte und Dokumentationsvermerk für Auftraggeber aufbauen: Beschaffungsbedarf, Markterkundung, Verfahrenswahl, Eignung, Wertung, Kommunikation, Entscheidungen und Nachvollziehbarkeit.

# Vergabeakte und Dokumentationsvermerk

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll eine prueffeste Vergabeakte erstellen oder lueckenhaftes Material reparieren. Er arbeitet für Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zuständigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Aktenstruktur, Dokumentationsvermerk, Lueckenliste, Haftungsampel.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` für Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `nachpruefungsantrag-powerdraft` für VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` für komplexe Mehrthemenfaelle.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `vergabekammer-termin-simulation`

**Fokus:** Vergabekammer-Termin simulieren: Fragenkatalog, Schwachstellen, Vergleichsfenster, Antragstaktik, Mandantenbriefing und Nachterminplan.

# Vergabekammer-Termin Simulation

## Zweck

Dieser Skill erweitert das Fachanwalt-Vergaberecht-Plugin zu einer echten Vergabe-Workbench. Er soll Mandanten und Anwalt auf VK-Termin oder Telefonkonferenz vorbereiten. Er arbeitet für Auftraggeber, Bieter, Beigeladene, Zuwendungsempfaenger, Projektsteuerer und Kanzleien, sofern die Perspektive zu Beginn klar markiert wird.

## Sofortmodus

1. Rolle klaeren: Auftraggeber, Bieter, Beigeladener, Foerdermittelempfaenger, Projektsteuerer oder Kanzlei.
2. Verfahrensstand klaeren: Markterkundung, Bekanntmachung, Angebotsphase, Wertung, Paragraph 134 GWB, Zuschlag, Vertrag, Nachpruefung, Beschwerde oder Schadensersatz.
3. Schwellenwert und Rechtsweg pruefen: Oberschwelle, Unterschwelle, Sektoren, Konzession, Verteidigung/Sicherheit, Foerdermittel oder Sonderregime.
4. Fristen sichern: Ruge, Angebotsfrist, Stillhaltefrist, 15-Tage-Frist nach Nichtabhilfe, Beschwerdefrist, Paragraph 135 GWB-Fristen.
5. Erst danach in die materielle Pruefung gehen.

## Arbeitsweise

- Baue zuerst eine kleine Tabelle mit `Tatsache`, `Beleg`, `rechtliche Bedeutung`, `Risiko`, `naechster Schritt`.
- Trenne strikt zwischen gesicherten Tatsachen, plausiblen Annahmen und offenen Pruefpunkten.
- Wenn der Nutzer Anfaenger ist, erklaere jedes vergaberechtliche Kunstwort in einem Satz und liefere danach sofort die Handlung.
- Wenn der Nutzer erfahren ist, liefere direkt Matrix, Schriftsatzkern, Vermerk oder Entscheidungsvorlage.
- Bei schwellenwert-, formular-, TED/eForms-, Wettbewerbsregister-, Landes- oder EU-Fragen einen Live-/Aktualitaetscheck verlangen, bevor Zahlen oder Formularlogik tragend verwendet werden.

## Pflicht-Output

- Kurzbild in drei Saetzen.
- Ampel: Frist, Zuständigkeit/Rechtsweg, Sachverhalt, Belege, Erfolgsaussicht, Kostenrisiko.
- Matrix oder Padlet-Block, wenn mehr als drei Themen/Fehler/Unterlagen betroffen sind.
- Konkreter naechster Schritt mit Adressat, Frist, benoetigten Anlagen und Entwurfsformat.

## Typische Outputs

Simulationsskript, Richter-/Kammerfragen, Antwortlinien, Vergleichsoptionen.

## Qualitaetsgates

- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Datum, Aktenzeichen und frei oder amtlich pruefbarer Quelle absichern.
- Keine ungeprueften Schwellenwerte. Fuer 2026/2027 sind die offiziellen EU-/nationalen Quellen vor tragender Verwendung zu pruefen.
- Keine pauschale Ruge. Jeder Vergabeverstoss braucht konkrete Tatsache, verletzte Regel, Kausalitaet/Chance und begehrte Abhilfe.
- Auftraggeberseitig immer dokumentieren: Warum durfte genau diese Entscheidung zu genau diesem Zeitpunkt getroffen werden?
- Bieterseitig immer taktisch pruefen: Rugen, nachfragen, Angebot abgeben, Nachpruefung, Vergleich oder Schadensersatz.

## Anschluss-Skills

- `vergabe-os-master-orchestrator` für Gesamtsteuerung.
- `schwellenwerte-2026-2027-livecheck` für Schwellenwert und Rechtsweg.
- `workflow-chronologie-und-belegmatrix` für Aktenarbeit.
- `nachpruefungsantrag-powerdraft` für VK-Verfahren.
- `mandantenpadlet-vergabe-canvas` für komplexe Mehrthemenfaelle.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.
